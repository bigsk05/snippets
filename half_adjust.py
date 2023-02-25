half_adjust = lambda n, u=0 : int(n * 10 ** u) / 10 ** u \
                              if n * 10 ** u - int(n * 10 ** u) < 0.5 \
                              else (int(n * 10 ** u) + 1) / 10 ** u