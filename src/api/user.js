import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/v2/security/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/v2/security/userinfo',
    method: 'get'
    // params: { token }
  })
}

// export function logout() {
//   return request({
//     url: '/v2/security/logout',
//     method: 'post'
//   })
// }
