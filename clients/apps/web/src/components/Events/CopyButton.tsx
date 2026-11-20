import { toast } from '@/components/Toast/use-toast'
import { useSafeCopy } from '@/hooks/clipboard'
import { Button } from '@repalis/orbit'
import { Check, Copy } from '@repalis/orbit/icons'
import { useEffect, useState } from 'react'

const COPIED_DURATION_MS = 1500

export const CopyButton = ({
  value,
  label = 'Copy',
}: {
  value: string
  label?: string
}) => {
  const [copied, setCopied] = useState(false)
  const safeCopy = useSafeCopy(toast)

  useEffect(() => {
    if (!copied) return
    const timeout = setTimeout(() => setCopied(false), COPIED_DURATION_MS)
    return () => clearTimeout(timeout)
  }, [copied])

  return (
    <Button
      size="icon"
      variant="ghost"
      className="h-6 w-6 [&_svg]:size-3!"
      aria-label={copied ? 'Copied' : label}
      title={copied ? 'Copied' : label}
      onClick={async () => {
        await safeCopy(value)
        setCopied(true)
      }}
    >
      {copied ? (
        <Check className="dark:text-repalis-500 text-gray-400" />
      ) : (
        <Copy />
      )}
    </Button>
  )
}
