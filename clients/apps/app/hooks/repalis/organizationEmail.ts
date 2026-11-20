import { useRepalisClient } from '@/providers/RepalisClientProvider'
import { queryClient } from '@/utils/query'
import { ClientResponseError, unwrap } from '@repalis/client'
import { skipToken, useMutation, useQuery } from '@tanstack/react-query'

const organizationEmailQueryKey = (organizationId?: string) => [
  'organization_email',
  organizationId,
]

export const useOrganizationEmail = (organizationId?: string) => {
  const { polar } = useRepalisClient()

  return useQuery({
    queryKey: organizationEmailQueryKey(organizationId),
    queryFn: organizationId
      ? () =>
          unwrap(
            repalis.GET('/v1/organizations/{id}/email/', {
              params: { path: { id: organizationId } },
            }),
          )
      : skipToken,
  })
}

export const useSendOrganizationEmailCode = (organizationId?: string) => {
  const { polar } = useRepalisClient()

  return useMutation({
    mutationFn: async () => {
      if (!organizationId) {
        throw new Error('organizationId is required to send a code')
      }
      const { error, response } = await repalis.POST(
        '/v1/organizations/{id}/email/send-code',
        { params: { path: { id: organizationId } } },
      )
      if (error) {
        throw new ClientResponseError(error, response)
      }
    },
    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: organizationEmailQueryKey(organizationId),
      })
    },
  })
}

export const useVerifyOrganizationEmail = (organizationId?: string) => {
  const { polar } = useRepalisClient()

  return useMutation({
    mutationFn: (code: string) => {
      if (!organizationId) {
        throw new Error('organizationId is required to verify the email')
      }
      return unwrap(
        repalis.POST('/v1/organizations/{id}/email/verify', {
          params: { path: { id: organizationId } },
          body: { code },
        }),
      )
    },
    onSuccess: (status) => {
      queryClient.setQueryData(
        organizationEmailQueryKey(organizationId),
        status,
      )
    },
  })
}
