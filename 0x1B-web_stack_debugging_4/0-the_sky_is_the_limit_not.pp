exec { 'fix--for-nginx':
  command => 'sed -i "s/worker_processes [0-9]*/worker_processes 4/;s/worker_connections [0-9]*/worker_connections 1024/;s/keepalive_timeout [0-9]*/keepalive_timeout 65/" /etc/nginx/nginx.conf && service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
