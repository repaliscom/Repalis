import LandingLayout from '@/components/Landing/LandingLayout'
import { NotFound } from '@/components/Landing/NotFound'
import { Suspense } from 'react'
import { RepalisThemeProvider } from './providers'

export default function RootNotFound() {
  return (
    <Suspense>
      <RepalisThemeProvider>
        <LandingLayout>
          <NotFound />
        </LandingLayout>
      </RepalisThemeProvider>
    </Suspense>
  )
}
