import { schemas } from '@repalis/client'
import { type StatusColor } from '@repalis/orbit'

export const seatStatusDisplayConfig: Record<
  schemas['SeatStatus'],
  [string, StatusColor]
> = {
  pending: ['Pending', 'yellow'],
  claimed: ['Claimed', 'green'],
  revoked: ['Revoked', 'gray'],
}
