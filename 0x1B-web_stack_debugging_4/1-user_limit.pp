exec { 'increase-file-descriptor-limit':
  command => '/bin/echo "holberton soft nofile 65536" >> /etc/security/limits.conf && /bin/echo "hoberton hard nofile 65536" >> /etc/security/limits.conf && /bin/echo "session required pam_limits.so" >> /etc/pam.d/common-session && /bin/echo "session required pam_limits.so" >> /etc/pam.d/common-session-noninteractive',
  unless  => '/bin/grep -q "holberton soft nofile 65536" /etc/security/limits.conf',
}
