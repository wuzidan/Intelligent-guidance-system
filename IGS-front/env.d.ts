/// <reference types="vite/client" />

// 环境变量类型声明
interface ImportMetaEnv {
  readonly VITE_APP_TITLE: string
  // 可以添加其他环境变量的类型声明
}

type ImportMeta = typeof import(meta)