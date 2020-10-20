import { UserManager } from 'oidc-client'

const auth = process.env.REACT_APP_AUTH
const clientId = process.env.REACT_APP_CLIENT_ID
const root = process.env.REACT_APP_CLIENT_ROOT
const responseType = process.env.REACT_APP_RESPONSE
const scopeProfile = process.env.REACT_APP_SCOPE

const settings = {
  authority: auth,
  client_id: clientId,
  redirect_uri: `${root}auth/oidc`,
  response_type: responseType,
  post_logout_redirect_uri: root,
  scope: scopeProfile,
}

export class AuthService {
  static instance = null

  constructor() {
    this.userManager = new UserManager(settings)
  }

  async getUser() {
    return await this.userManager.getUser()
  }

  async login() {
    return await this.userManager.signinRedirect()
  }

  signinRedirectCallback() {
    // console.log(this.userManager.signinRedirectCallback())
    return  this.userManager.signinRedirectCallback()
  }

  logout = () => {
    this.userManager.signoutRedirect()
  }

  signoutRedirectCallback() {
    return this.userManager.signoutRedirectCallback()
  }

  static getInstance() {
    if (AuthService.instance == null) {
      AuthService.instance = new AuthService()
    }
    return AuthService.instance
  }
}
