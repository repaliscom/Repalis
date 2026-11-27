import type { schemas } from '@repalis/client'
import { DEFAULT_LOCALE, type AcceptedLocale } from '@repalis/i18n'
import { getMeterUnitFormat } from '@repalis/ui/lib/meterUnit'
import { cn } from '@repalis/ui/lib/utils'
import { getStartingUnitAmount, type MeteredPrice } from '../utils/product'
import MeteredRate from './MeteredRate'

interface MeteredPriceLabelProps {
  price: MeteredPrice
  locale?: AcceptedLocale
  discount?: schemas['CheckoutPublic']['discount']
}

const MeteredPriceLabel: React.FC<MeteredPriceLabelProps> = ({
  price,
  locale = DEFAULT_LOCALE,
  discount,
}) => {
  const { scale, label } = getMeterUnitFormat(price.meter.unit ?? 'scalar', {
    customLabel: price.meter.custom_label,
    customMultiplier: price.meter.custom_multiplier,
    locale,
  })

  return (
    <div className="flex flex-row items-baseline gap-x-1">
      <MeteredRate
        amount={getStartingUnitAmount(price) * scale}
        currency={price.price_currency}
        locale={locale}
        discount={discount}
      />
      <span
        className={cn(
          'dark:text-repalis-400 text-[max(12px,0.5em)] text-gray-500',
          price.meter.unit === 'custom' ? 'lowercase' : '',
        )}
      >
        / {label}
      </span>
    </div>
  )
}

export default MeteredPriceLabel
