import BaseServices from './baseServices'

export default class UserServices extends BaseServices {
  constructor(resourcePath = 'users') {
    super(resourcePath)
  }
}
