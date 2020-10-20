import url from 'url'
import querystring from 'querystring'

import { config } from '../config/config'

export function validateIfNotNull(obj, key, value) {
  if (value) obj[key] = value
}

export default class BaseServices {
  resourcePath = null

  constructor(path) {
    this.resourcePath = path
  }

  getQueryOptions(options = {}) {
    const { page, limit, search } = options
    const queryOptions = {}

    validateIfNotNull(queryOptions, 'page', page)
    validateIfNotNull(queryOptions, 'limit', limit)
    validateIfNotNull(queryOptions, 'search', search)

    const query = querystring.encode(queryOptions)
    return query ? `?${query}` : ''
  }

  getAll() {
    return { url: url.resolve(config, this.resourcePath) }
  }

  get(id) {
    return { url: url.resolve(config, `${this.resourcePath}/${id}`) }
  }

  search(search) {
    const value = this.getQueryOptions({ search })
    return { url: url.resolve(config, `${this.resourcePath}${value}`) }
  }

  pagination(page, limit) {
    const pagination = this.getQueryOptions({ page, limit })
    return {
      url: url.resolve(config, `${this.resourcePath}${pagination}`),
    }
  }

  getTourView(id) {
    return { url: url.resolve(config, `${this.resourcePath}/${id}/tourview`) }
  }

  experiences(id, page, limit) {
    const pagination = this.getQueryOptions({ page, limit })
    return {
      url: url.resolve(
        config,
        `${this.resourcePath}/${id}/experiences${pagination}`,
      ),
    }
  }

  favorites(userId, token) {
    const options = {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
    }
    return {
      url: url.resolve(config, `${this.resourcePath}/${userId}/favorites`),
      options,
    }
  }
}
