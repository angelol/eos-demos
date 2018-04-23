var ipfs = window.IpfsApi('localhost', '5001');

var hash;
var error;

function submit(event) {
    event.preventDefault();

    let text = $('textarea').val();
    let buffer = ipfs.Buffer.from(text);
    var hash;
    ipfs.files.add(buffer, { pin: true }, (err, ipfsHash) => {
        let hash = ipfsHash[0].hash;
        eos.transaction({
            actions: [
                {
                    account: account,
                    name: 'addblog',
                    authorization: [{
                    actor: account,
                    permission: 'active'
                }],
                data: {
                    author: $("input[name=author]").val(),
                    title: $("input[name=title]").val(),
                    hash: hash
                }
                }
            ]
        }).then(x => {

        });
    });
};

$(function() {
    $('form').submit(submit);
});
