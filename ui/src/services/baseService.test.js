import { TourServices } from '.'
import { config } from '../config/config'

const services = new TourServices()
const id = '5ec573d6f235707135952a94'

describe('./services/baseServices.js', () => {
  describe('Validate params', () => {
    it('should call api with all params', () => {
      const options = services.experiences(id, 1, 2)
      expect(options).toEqual({
        url: `${config}tours/${id}/experiences?page=1&limit=2`,
      })
    })

    it('should call api when limit is null', () => {
      const option = services.experiences(id, 1, null)
      expect(option).toEqual({
        url: `${config}tours/${id}/experiences?page=1`,
      })
    })

    it('should call api when page is null', () => {
      const option = services.experiences(id, null, 2)
      expect(option).toEqual({
        url: `${config}tours/${id}/experiences?limit=2`,
      })
    })

    it('should call api when page and limit are null', () => {
      const option = services.experiences(id, null, null)
      expect(option).toEqual({
        url: `${config}tours/${id}/experiences`,
      })
    })
  })
})
