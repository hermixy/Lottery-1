'use strict'

import axios from 'axios'
import qs from 'qs'

axios.interceptors.request.use(config => {
  // loading
  return config
}, error => {
  return Promise.reject(error)
})

axios.interceptors.response.use(response => {
  return response
}, error => {
  return Promise.resolve(error.response)
})

function checkStatus (response) {
  // loading
  // 如果http状态码正常，则直接返回数据
  // console.log('checkStatus', response)
  if (response && (response.status === 200)) {
    if (response.data != null && response.data.status === 200) {
      return response.data
    } else {
      return {
        status: response.data.status,
        msg: response.data.msg
      }
    }
  }
  // 异常状态下，把错误信息返回去
  return {
    status: -404,
    msg: '网络异常'
  }
}

function checkCode (res) {
  // 如果code异常(这里已经包括网络错误，服务器错误，后端抛出的错误)，可以弹出一个错误提示，告诉用户
  // console.log('checkCode', res)
  if (res.status !== 200) {
    this.$Notice.warning({
      title: res.msg
      // desc: nodesc ? '' : 'Here is the notification description. Here is the notification description. '
    })
  }
  return res
}

export default {
  isSuccess (data) {
    if (data.status === 200) {
      return true
    } else {
      return false
    }
  },
  post (url, data) {
    return axios({
      method: 'post',
      baseURL: 'http://119.27.171.189',
      url,
      data: qs.stringify(data),
      timeout: 10000,
      headers: {
        // 'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
      }
    }).then(
      (response) => {
        return checkStatus(response)
      }
    ).then(
      (res) => {
        return checkCode(res)
      }
    )
  },
  get (url, params) {
    return axios({
      method: 'get',
      baseURL: 'http://119.27.171.189',
      url,
      params, // get 请求时带的参数
      timeout: 10000,
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      }
    }).then(
      (response) => {
        return checkStatus(response)
      }
    ).then(
      (res) => {
        return checkCode(res)
      }
    )
  }
}
