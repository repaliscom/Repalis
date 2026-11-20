import { useRepalisClient } from '@/providers/RepalisClientProvider'
import { useSession } from '@/providers/SessionProvider'
import { schemas, unwrap } from '@repalis/client'
import { useQuery } from '@tanstack/react-query'
import { createContext, PropsWithChildren, useContext } from 'react'

export type User = schemas['UserInfoUser']

interface UserContextValue {
  user: User | undefined
  isLoading: boolean
}

const UserContext = createContext<UserContextValue>({
  user: undefined,
  isLoading: true,
})

export const useUser = () => useContext(UserContext)

export function UserProvider({ children }: PropsWithChildren) {
  const { session } = useSession()
  const { polar } = useRepalisClient()

  const { data: user, isLoading } = useQuery({
    queryKey: ['userinfo'],
    queryFn: async () => {
      const data = await unwrap(polar.GET('/v1/oauth2/userinfo'))
      return data as User
    },
    enabled: !!session,
  })

  return (
    <UserContext.Provider value={{ user, isLoading }}>
      {children}
    </UserContext.Provider>
  )
}
