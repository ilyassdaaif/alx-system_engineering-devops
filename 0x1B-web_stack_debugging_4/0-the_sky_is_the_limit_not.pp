exec { 'fix--for-nginx':
  command => 'sed -i "s/worker_connections 768;/worker_connections 4096;/g" /etc/nginx/nginx.conf && nginx -s reload',
  onlyif  => 'grep -q "worker_connections 768;" /etc/nginx/nginx.conf',
}
