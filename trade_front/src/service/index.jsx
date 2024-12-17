import axios from "axios";
const { baseURL } = window;

const root = () => {
  return axios({
    baseURL,
    method: 'get',
    url: '/'
  })
};

const user = {
  updateInfo: (email, password, nickname, gender, age, contact, reputation) => {
    return axios({
      baseURL,
      method: 'put',
      url: '/user/updateInfo',
      data: {
        email,
        password,
        nickname,
        gender,
        age,
        contact,
        reputation
      }
    })
  },
  getInfo: () => {
    return axios({
      baseURL,
      method: 'get',
      url: '/user/getInfo',
    })
  },
  auth: (email, password) => {
    return axios({
      baseURL,
      method: 'post',
      url: '/user/auth',
      data: {
        email,
        password,
      }
    })
  },
  check: () => {
    return axios({
      baseURL,
      method: 'post',
      url: '/user/check'
    })
  },
  register: (nickname, password, email) => {
    return axios({
      baseURL,
      method: 'post',
      url: '/user/register',
      data: {
        nickname,
        password,
        email
      }
    })
  },
  
}

const record = {
  getInfo: (id) => {
    return axios({
      baseURL,
      method: 'get',
      url: '/record/getInfo',
      params: {
        id
      }
    })
  },
  updateInfo: (id, buyer_id, seller_id, commodity_id, quantity, total, status) => {
    return axios({
      baseURL,
      method: 'put',
      url: '/record/updateInfo',
      data: {
        id,
        buyer_id,
        seller_id,
        commodity_id,
        quantity,
        total,
        status
      }
    })
  }
}

const commodity = {
  
  getInfo: (id) => {
    return axios({
      baseURL,
      method: 'get',
      url: '/commodity/getInfo',
      params: {
        id
      }
    })
  },
  updateInfo: (id, user_id, name, description, price, category, status, image) => {
    return axios({
      baseURL,
      method: 'put',
      url: '/commodity/updateInfo',
      data: {
        id,
        user_id,
        name,
        description,
        price,
        category,
        status,
        image
      }
    })
  },
}


export const service = {user, root, 
                        record, commodity}