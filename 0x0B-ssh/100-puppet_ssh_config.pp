# Pupppet file to configurate SSH conection without password
file_line { 'No-password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}
