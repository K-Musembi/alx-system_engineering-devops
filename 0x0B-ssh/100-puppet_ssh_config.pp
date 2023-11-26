# Configure SSH client configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "\
    Host *
        IdentityFile ~/.ssh/school
        PreferredAuthentications publickey
        PasswordAuthentication no
  ",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
