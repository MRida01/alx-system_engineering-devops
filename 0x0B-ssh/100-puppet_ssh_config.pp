# Configures SSH server

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no',
  ensure  => present,
  match   => '^PasswordAuthentication.*$',
}

file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  ensure  => present,
  match   => '^#?IdentityFile.*$',
}