/* global process */
const TYPE_CHECKED_IN_CI = process.env.VERCEL === '1' || Boolean(process.env.CI)

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  reactCompiler: true,
  experimental: {
    optimizePackageImports: ['@repalis/orbit/icons'],
  },
  transpilePackages: ['@repalis/orbit', 'shiki'],

  ...(TYPE_CHECKED_IN_CI && {
    typescript: { ignoreBuildErrors: true },
  }),
}

export default nextConfig
