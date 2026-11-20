/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  reactCompiler: true,
  experimental: {
    optimizePackageImports: ['@repalis/orbit/icons'],
  },
  transpilePackages: ['@repalis/orbit', 'shiki'],
}

export default nextConfig
