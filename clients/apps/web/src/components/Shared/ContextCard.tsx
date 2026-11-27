import ShadowBox from '@repalis/ui/components/atoms/ShadowBox'
import { PropsWithChildren } from 'react'

export const ContextCard = ({ children }: PropsWithChildren) => (
  <ShadowBox className="dark:border-repalis-800 flex flex-col gap-4 border-gray-200 bg-white p-6 md:shadow-xs lg:rounded-2xl">
    {children}
  </ShadowBox>
)
