FROM oven/bun:latest
WORKDIR /app

COPY . .

RUN bun install
RUN bunx --bun astro build

ENV HOST=0.0.0.0
ENV PORT=4321
EXPOSE 4321
CMD bunx --bun astro preview --host 0.0.0.0 --port 4321
