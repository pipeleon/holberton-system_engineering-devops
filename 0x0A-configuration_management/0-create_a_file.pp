#Manifest in Puppet to create a file in /tmp

$doc_root = '/tmp/school'

file { $doc_root:
  ensure  => 'file',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
