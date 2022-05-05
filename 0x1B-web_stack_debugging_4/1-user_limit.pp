# Puppet code to increased the limit of open files for holberton user
exec { 'change-os-configuration-for-holberton-user':
    command => 'sed -i s/5/4096/ /etc/security/limits.conf && sed -i s/4/4096/ /etc/security/limits.conf',
    path    => ['/bin', '/usr/bin']
}
