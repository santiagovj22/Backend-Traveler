const key = process.env.REACT_APP_LOGIN

export default function isLogin() {
  return !!sessionStorage.getItem(key)
}
