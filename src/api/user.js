import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/v1/security/login/ex',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/v1/security/userinfo',
    method: 'get'
    // params: { token }
  })
}

// export function logout() {
//   return request({
//     url: '/v1/security/logout',
//     method: 'post'
//   })
// }
