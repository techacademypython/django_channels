FROM redis:4.0.11

ENV REDIS_PASSWORD A9KvmBL89uK9VZMz

CMD ["sh", "-c", "exec redis-server --requirepass \"$REDIS_PASSWORD\""]