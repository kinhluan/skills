const base = import.meta.env.BASE_URL.replace(/\/$/, "");

export function withBase(pathname = "/"): string {
  const normalized = pathname.startsWith("/") ? pathname : `/${pathname}`;
  return `${base}${normalized}`;
}

export const githubRepository = "https://github.com/kinhluan/skills";
