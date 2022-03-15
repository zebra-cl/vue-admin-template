import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/v1/security/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/api/v1/security/userinfo',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/api/v1/security/logout',
    method: 'post'
  })
}
