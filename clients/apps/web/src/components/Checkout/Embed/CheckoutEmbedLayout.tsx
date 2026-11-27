import type { schemas } from '@repalis/client'
import type { TextDirection } from '@repalis/i18n'
import CheckoutEmbedClose from './CheckoutEmbedClose'
import CheckoutEmbedLoaded from './CheckoutEmbedLoaded'

const CheckoutEmbedLayout = ({
  children,
  checkout,
  theme,
  dir = 'ltr',
}: React.PropsWithChildren<{
  checkout: schemas['CheckoutPublic']
  theme?: 'light' | 'dark'
  dir?: TextDirection
}>) => {
  const colorScheme = theme === 'dark' ? 'dark' : 'light'
  return (
    <div
      className={colorScheme}
      dir={dir}
      id="repalis-embed-layout"
      data-repalis-embed-theme={colorScheme}
    >
      <div className="flex h-full w-full items-center justify-center p-0 md:p-6 dark:text-white">
        <div className="h-full w-full max-w-lg" id="repalis-embed-content">
          {children}
        </div>
      </div>
      <CheckoutEmbedClose checkout={checkout} />
      <CheckoutEmbedLoaded checkout={checkout} />
    </div>
  )
}

export default CheckoutEmbedLayout
