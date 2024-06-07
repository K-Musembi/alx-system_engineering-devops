# Puppet manifest to diagnose and fix a 500 error in Apache

package { 'strace':
  ensure => installed,
}

exec { 'trace_apache':
  command => '/usr/bin/strace -o /tmp/strace_apache.log -f -e trace=file -p $(pgrep -o httpd || pgrep -o apache2)',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  require => Package['strace'],
}

exec { 'analyze_strace_log':
  command => '/bin/grep -i "Permission denied" /tmp/strace_apache.log > /tmp/strace_analysis.log',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  require => Exec['trace_apache'],
}

exec { 'fix_permissions':
  command => 'chmod -R 755 /var/www/html',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif  => 'grep -q "Permission denied" /tmp/strace_analysis.log',
  require => Exec['analyze_strace_log'],
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix_permissions'],
}
