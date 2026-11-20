import { useRepalisClient } from '@/providers/RepalisClientProvider'
import { useSession } from '@/providers/SessionProvider'
import { queryClient } from '@/utils/query'
import { schemas, unwrap } from '@repalis/client'
import { useMutation, useQuery, UseQueryResult } from '@tanstack/react-query'
import { Platform } from 'react-native'

export const useCreateNotificationRecipient = () => {
  const { repalis } = useRepalisClient()

  return useMutation({
    mutationFn: async (expoPushToken: string) => {
      return unwrap(
        repalis.POST('/v1/notifications/recipients', {
          body: {
            expo_push_token: expoPushToken,
            platform: Platform.OS as 'ios' | 'android',
          },
        }),
      )
    },
    onSuccess: (result, variables, context) => {
      queryClient.invalidateQueries({ queryKey: ['notification_recipient'] })
      queryClient.invalidateQueries({ queryKey: ['notification_recipients'] })
    },
  })
}

export const useGetNotificationRecipient = (
  expoPushToken: string | undefined,
) => {
  const { session } = useSession()
  const { repalis } = useRepalisClient()

  return useQuery({
    queryKey: ['notification_recipient', expoPushToken],
    queryFn: async () => {
      const response = await unwrap(
        repalis.GET('/v1/notifications/recipients', {
          params: {
            query: {
              expo_push_token: expoPushToken,
            },
          },
        }),
      )

      return response.items?.[0] ?? null
    },
    enabled: !!expoPushToken && !!session,
    throwOnError: false,
  })
}

export const useDeleteNotificationRecipient = () => {
  const { repalis } = useRepalisClient()

  return useMutation({
    mutationFn: async (id: string) => {
      return repalis
        .DELETE('/v1/notifications/recipients/{id}', {
          params: {
            path: {
              id,
            },
          },
        })
        .finally(() => {
          queryClient.invalidateQueries({
            queryKey: ['notification_recipients'],
          })
          queryClient.invalidateQueries({
            queryKey: ['notification_recipient'],
          })
        })
    },
  })
}

export type Notification = schemas['NotificationsList']['notifications'][number]

export type MaintainerNewPaidSubscriptionNotificationPayload =
  schemas['MaintainerNewPaidSubscriptionNotificationPayload']
export type MaintainerNewTrialNotificationPayload =
  schemas['MaintainerNewTrialNotificationPayload']
export type MaintainerSubscriptionCancellationNotificationPayload =
  schemas['MaintainerSubscriptionCancellationNotificationPayload']
export type MaintainerNewProductSaleNotificationPayload =
  schemas['MaintainerNewProductSaleNotificationPayload']
export type MaintainerAccountCreditsGrantedNotificationPayload =
  schemas['MaintainerAccountCreditsGrantedNotificationPayload']
export type MaintainerSubscriptionRenewalNotificationPayload =
  schemas['MaintainerSubscriptionRenewalNotificationPayload']
export type MaintainerFileFlaggedMaliciousNotificationPayload =
  schemas['MaintainerFileFlaggedMaliciousNotificationPayload']

export const useListNotifications = (): UseQueryResult<
  schemas['NotificationsList'],
  Error
> => {
  const { repalis } = useRepalisClient()
  const { session } = useSession()

  return useQuery({
    queryKey: ['notifications'],
    queryFn: () => unwrap(repalis.GET('/v1/notifications')),
    enabled: !!session,
  })
}

export const useNotificationsMarkRead = () => {
  const { repalis } = useRepalisClient()

  return useMutation({
    mutationFn: (variables: { notificationId: string }) =>
      unwrap(
        repalis.POST('/v1/notifications/read', {
          body: { notification_id: variables.notificationId },
        }),
      ),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['notifications'] })
    },
  })
}
