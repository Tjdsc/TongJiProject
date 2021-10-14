// 封装AXIOS，并对get、post做封装
import axios from 'axios';
import { Message } from 'element-ui';
import QS from 'qs';

/**
 * 相应时间修改为60秒
 */
const instance = axios.create({
  timeout: 60000,
});
instance.defaults.withCredentials = true;

const pending = []; // 声明一个数组用于存储每个ajax请求的取消函数和ajax标识
const CancelToken = axios.CancelToken;
const removePending = (config) => {
  for (const p in pending) {
    if (pending[p].u === `${config.url}&${config.method}`) { // 当当前请求在数组中存在时执行函数体
      pending[p].f(); // 执行取消操作
      pending.splice(p, 1); // 把这条记录从数组中移除
    }
  }
};

// 添加请求拦截器
axios.interceptors.request.use((config) => {
  removePending(config); // 在一个ajax发送前执行一下取消操作
  config.cancelToken = new CancelToken((c) => {
    // 用接口名拼接请求方式进行标记
    pending.push({ u: `${config.url}&${config.method}`, f: c });
  });
  return config;
}, error => Promise.reject(error));

instance.interceptors.response.use(
  (res) => {
    let R = null;
    if (res.status === 200) {
      const {
        data: {
          data: resData, success = false, errorCode = '', errorMsg = '',
        },
      } = res;
      if (success) {
        R = resData;
        return Promise.resolve(R);
      }
      R = [errorCode, errorMsg];
      return Promise.reject(R);
    }
    return `error${res}`;
  },
  (error) => {
    Message.error({
      message: error.message || '接口出错',
    });
    if (error.response) {
      return Promise.reject(error.response.data);
    }
    return Promise.reject([-1, '未知错误']);
  },
);

export default {
  /**
   * GET
   * @param url
   * @param params
   * @return {Promise<any>}
   */
  get(url, params) {
    return new Promise((resolve, reject) => {
      instance.get(url, { params })
        .then((res) => {
          resolve(res);
        })
        .catch((err) => {
          console.error(`GET请求url(${url})失败,错误如下:`);
          console.error(err);
          reject(err);
        });
    });
  },
  /**
   * POST请求
   * @param url
   * @param params
   * @param config
   * @return {Promise<any>}
   */
  post(url, params = {}, config = {}) {
    return new Promise((resolve, reject) => {
      // console.debug('post params=',params);
      instance.post(url, QS.stringify({ ...params }), config)
        .then((res) => {
          resolve(res);
        })
        .catch((err) => {
          console.error(`POST请求url(${url})失败,错误如下:`);
          reject(err);
        });
    });
  },
  /**
   * 使用JSON对象POST给服务器
   * @param url
   * @param params
   * @param config
   * @return {Promise<any>}
   */
  postJson(url, params = {}, config = {}) {
    return new Promise((resolve, reject) => {
      const { headers = {} } = config;
      config.headers = { 'Content-Type': 'application/json', ...headers };
      instance.post(url, params, config)
        .then((res) => {
          resolve(res);
        })
        .catch((err) => {
          console.error(`POST请求url(${url})失败,错误如下:`);
          console.error(err);
          reject(err);
        });
    });
  },
  /**
   * 使用FORM方式POST服务器
   * @param url
   * @param formData
   * @param config
   * @return {Promise<any>}
   */
  postForm(url, formData, config = {}) {
    return new Promise((resolve, reject) => {
      const { headers = {} } = config;
      config.headers = { 'Content-Type': 'multipart/form-data', ...headers };
      instance.post(url, formData, config)
        .then((res) => {
          resolve(res);
        })
        .catch((err) => {
          console.error(`POST请求url(${url})失败,错误如下:`);
          console.error(err);
          reject(err);
        });
    });
  },
};
