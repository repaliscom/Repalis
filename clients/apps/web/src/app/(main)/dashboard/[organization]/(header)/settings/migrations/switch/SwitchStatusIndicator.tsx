import { Status } from '@repalis/orbit'
import { SwitchRow } from './switchRows'
import { switchStatus } from './switchStatus'

export function SwitchStatusIndicator({ row }: { row: SwitchRow }) {
  const { label, color } = switchStatus(row)
  return <Status status={label} color={color ?? 'gray'} size="small" />
}
