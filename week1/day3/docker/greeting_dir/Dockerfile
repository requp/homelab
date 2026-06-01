FROM ubuntu:26.04
COPY names.txt ./names.txt
COPY greeting.sh ./greeting.sh
RUN sort -u names.txt > clean_names.txt && \
	chmod +x greeting.sh

ENTRYPOINT ["./greeting.sh"]
CMD ["Hello"]
