infile="Chall_2.pcapng"
outfile=payload
ext=txt

rm -f ${outfile}_all.${ext}

for stream in $(tshark -nlr $infile -Y tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | sed 's/\r//')
do
    #echo "Processing stream $stream: ${outfile}_${stream}.${ext}"
    tshark -nlr $infile -qz "follow,tcp,raw,$stream" | tail -n +7 | sed 's/^\s\+//g' | xxd -r -p >> ${outfile}_all.${ext}
done
