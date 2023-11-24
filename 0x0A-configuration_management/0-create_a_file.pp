# Creating a file with permission, owner and group

file { '/tmp/school':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => "I love Puppet\n",
}
