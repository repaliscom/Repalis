import { RepalisThemeProvider } from '@/app/providers'
import type { schemas } from '@repalis/client'
import type { TextDirection } from '@repalis/i18n'
import CheckoutDirectionProvider from './CheckoutDirectionProvider'
import CheckoutEmbedLayout from './Embed/CheckoutEmbedLayout'

const CheckoutLayout = ({
  children,
  checkout,
  embed,
  theme,
  dir = 'ltr',
}: React.PropsWithChildren<{
  checkout: schemas['CheckoutPublic']
  embed: boolean
  theme?: 'light' | 'dark'
  dir?: TextDirection
}>) => {
  if (embed) {
    return (
      <CheckoutDirectionProvider dir={dir}>
        <CheckoutEmbedLayout checkout={checkout} theme={theme} dir={dir}>
          {children}
        </CheckoutEmbedLayout>
      </CheckoutDirectionProvider>
    )
  }

  return (
    <CheckoutDirectionProvider dir={dir}>
      <RepalisThemeProvider>
        <div
          dir={dir}
          className="md:dark:bg-repalis-950 dark:bg-repalis-900 h-full min-h-screen bg-white md:bg-gray-50 dark:text-white"
        >
          {children}
        </div>
      </RepalisThemeProvider>
    </CheckoutDirectionProvider>
  )
}

export default CheckoutLayout
