import { useRepalisClient } from '@/providers/RepalisClientProvider'
import { queryClient } from '@/utils/query'
import { operations, schemas, unwrap } from '@repalis/client'
import { useInfiniteQuery, useMutation, useQuery } from '@tanstack/react-query'

export const useSubscription = (id: string) => {
  const { repalis } = useRepalisClient()

  return useQuery({
    queryKey: ['subscription', id],
    queryFn: () =>
      unwrap(repalis.GET('/v1/subscriptions/{id}', { params: { path: { id } } })),
  })
}

export const useSubscriptions = (
  organizationId?: string,
  parameters?: Omit<
    operations['subscriptions:list']['parameters']['query'],
    'organization_id'
  >,
) => {
  const { repalis } = useRepalisClient()

  return useInfiniteQuery({
    queryKey: ['subscriptions', { organizationId, ...(parameters || {}) }],
    queryFn: async ({ pageParam = 1 }) =>
      unwrap(
        repalis.GET('/v1/subscriptions/', {
          params: {
            query: {
              organization_id: organizationId,
              ...(parameters || {}),
              page: pageParam,
            },
          },
        }),
      ),
    enabled: !!organizationId,
    initialPageParam: 1,
    getNextPageParam: (lastPage, pages) => {
      if (lastPage.items.length === 0) return undefined
      return pages.length + 1
    },
  })
}

const SUBSCRIPTION_UPDATE_HEADERS = { 'Repalis-Version': '2027-01' }

export const useUpdateSubscription = (id: string) => {
  const { repalis } = useRepalisClient()

  return useMutation({
    mutationFn: (body: schemas['SubscriptionUpdate']) =>
      repalis.PATCH('/v1/subscriptions/{id}', {
        params: { path: { id } },
        body,
        headers: SUBSCRIPTION_UPDATE_HEADERS,
      }),
    onSuccess: (data, variables) => {
      queryClient.setQueryData(['subscription', id], data.data)

      queryClient.invalidateQueries({
        queryKey: ['subscriptions'],
      })
    },
  })
}
