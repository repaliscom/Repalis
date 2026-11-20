import { schemas } from '@repalis/client'
import { ReadonlyRequestCookies } from 'next/dist/server/web/spec-extension/adapters/request-cookies'

const lastVisitedOrg = 'last_visited_org'
export const REPALIS_ENV_COOKIE = 'repalis_env'

export type RepalisEnv = 'production' | 'sandbox'

export const setLastVisitedOrg = (
  organization: string,
  maxAge: number = 30 * 86400, // Expires in 30 days
) => {
  document.cookie = `${lastVisitedOrg}=${organization}; max-age=${maxAge}; path=/`
}

export const getLastVisitedOrg = (
  cookies: ReadonlyRequestCookies,
  organizations: schemas['Organization'][],
): schemas['Organization'] | undefined => {
  const lastVisitedOrgSlug = cookies.get(lastVisitedOrg)?.value
  if (!lastVisitedOrgSlug) {
    return undefined
  }
  return organizations.find((org) => org.slug === lastVisitedOrgSlug)
}

export const setLastVisitedEnv = (
  env: PolarEnv,
  maxAge: number = 30 * 60, // Expires in 30 minutes
) => {
  const hostname = window.location.hostname
  const domainAttr = hostname.endsWith('.repalis.com') ? '; domain=.repalis.com' : ''
  const secureAttr = window.location.protocol === 'https:' ? '; secure' : ''
  document.cookie = `${REPALIS_ENV_COOKIE}=${env}; max-age=${maxAge}; path=/; samesite=lax${domainAttr}${secureAttr}`
}
