'use client'

import {
  RepalisEmbedPaymentMethod,
  type EmbedPaymentMethodErrorCode,
} from '@repalis/checkout/payment-method'
import {
  DEFAULT_LOCALE,
  useTranslations,
  type AcceptedLocale,
} from '@repalis/i18n'
import { useEffect } from 'react'

const ERROR_TRANSLATION_KEYS = {
  invalid_request: 'embedPaymentMethod.errors.invalidRequest',
  unauthorized: 'embedPaymentMethod.errors.unauthorized',
  processing_failed: 'embedPaymentMethod.errors.processingFailed',
  unknown: 'embedPaymentMethod.errors.unknown',
} as const satisfies Record<EmbedPaymentMethodErrorCode, string>

interface Props {
  code: EmbedPaymentMethodErrorCode
  embedOrigin?: string
  locale?: AcceptedLocale
  theme?: 'light' | 'dark'
}

export const EmbedError = ({
  code,
  embedOrigin,
  locale = DEFAULT_LOCALE,
  theme,
}: Props) => {
  const t = useTranslations(locale)

  useEffect(() => {
    if (!embedOrigin) return
    RepalisEmbedPaymentMethod.postMessage({ event: 'error', code }, embedOrigin)
    RepalisEmbedPaymentMethod.postMessage({ event: 'loaded' }, embedOrigin)
  }, [code, embedOrigin])

  return (
    <p
      role="alert"
      className="p-4 text-center text-sm text-red-500"
      data-polar-embed-theme={theme === 'dark' ? 'dark' : 'light'}
    >
      {t(ERROR_TRANSLATION_KEYS[code])}
    </p>
  )
}
