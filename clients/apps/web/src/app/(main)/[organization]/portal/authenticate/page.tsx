import { getServerSideAPI } from '@/utils/client/serverside'
import { getOrganizationOrNotFound } from '@/utils/customerPortal'
import type { Metadata } from 'next'
import AuthenticatePage from './AuthenticatePage'

export async function generateMetadata(props: {
  params: Promise<{ organization: string }>
}): Promise<Metadata> {
  const params = await props.params
  const api = await getServerSideAPI()
  const { organization } = await getOrganizationOrNotFound(
    api,
    params.organization,
  )

  return {
    title: `Customer portal | ${organization.name}`, // " | Repalis is added by the template"
    openGraph: {
      title: `Customer portal | ${organization.name} on Repalis`,
      description: `Customer portal | ${organization.name} on Repalis`,
      siteName: 'Repalis',
      type: 'website',
      images: [
        {
          url: `https://repalis.com/og?org=${organization.slug}`,
          width: 1200,
          height: 630,
        },
      ],
    },
    twitter: {
      images: [
        {
          url: `https://repalis.com/og?org=${organization.slug}`,
          width: 1200,
          height: 630,
          alt: `${organization.name} on Repalis`,
        },
      ],
      card: 'summary_large_image',
      title: `Customer portal | ${organization.name} on Repalis`,
      description: `Customer portal | ${organization.name} on Repalis`,
    },
  }
}

export default async function Page(props: {
  params: Promise<{ organization: string }>
  searchParams: Promise<{ customer_session_token?: string }>
}) {
  const { customer_session_token, ...searchParams } = await props.searchParams
  const params = await props.params
  const api = await getServerSideAPI(customer_session_token)
  const { organization } = await getOrganizationOrNotFound(
    api,
    params.organization,
    searchParams,
  )

  return <AuthenticatePage organization={organization} />
}
