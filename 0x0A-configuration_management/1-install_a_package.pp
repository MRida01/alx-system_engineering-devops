#Installs flask from pip3
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => ['/usr/bin'],
  refreshonly => true,
  subscribe   => Package['python3-pip'],
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Exec['install_flask'],
}
