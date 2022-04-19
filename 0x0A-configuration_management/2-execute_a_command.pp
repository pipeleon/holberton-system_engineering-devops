#Manifest in Puppet to stop killmenow

exec { 'killing':
  command => 'pkill killmenow',
  provider => 'shell'
}
