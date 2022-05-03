# Puppet code to automate the fix of Wordpress configuration
exec { 'fix_wordpress':
    command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php && sudo service apache2 restart',
    path    => ['/bin', '/usr/bin']
}
