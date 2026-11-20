import { useRepalisClient } from '@/providers/RepalisClientProvider'
import { schemas, unwrap } from '@repalis/client'
import {
  skipToken,
  useMutation,
  useQuery,
  useQueryClient,
} from '@tanstack/react-query'

const NOTIFICATION_SETTINGS_HEADERS = { 'Repalis-Version': '2027-01' }

export const useUserOrganizationNotificationSettings = (
  organizationId?: string,
) => {
  const { polar } = useRepalisClient()

  return useQuery({
    queryKey: ['user', 'notificationSettings', organizationId],
    queryFn: organizationId
      ? () =>
          unwrap(
            repalis.GET(
              '/v1/users/me/organizations/{organization_id}/notification-settings',
              {
                params: { path: { organization_id: organizationId } },
                headers: NOTIFICATION_SETTINGS_HEADERS,
              },
            ),
          )
      : skipToken,
  })
}

export const useUpdateUserOrganizationNotificationSettings = () => {
  const { polar } = useRepalisClient()
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({
      organizationId,
      notification_settings,
    }: {
      organizationId: string
      notification_settings: schemas['OrganizationNotificationSettings']
    }) =>
      unwrap(
        repalis.PATCH(
          '/v1/users/me/organizations/{organization_id}/notification-settings',
          {
            params: { path: { organization_id: organizationId } },
            body: { notification_settings },
            headers: NOTIFICATION_SETTINGS_HEADERS,
          },
        ),
      ),
    onSettled: (_data, _error, variables) => {
      queryClient.invalidateQueries({
        queryKey: ['user', 'notificationSettings', variables.organizationId],
      })
    },
  })
}
