# Puppet code to increased the limit of files per (worker) process
exec { 'fix-request':
    command => 'sed -i s/15/4096/ /etc/default/nginx && sudo service nginx restart',
    path    => ['/bin', '/usr/bin']
}
