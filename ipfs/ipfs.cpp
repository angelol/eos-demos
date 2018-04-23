#include <eosiolib/eosio.hpp>
#include <eosiolib/print.hpp>

using namespace eosio;
using namespace std;

class ipfs : public contract {
    using contract::contract;

    public:
        ipfs(account_name self)
        :contract(self),
        blogs(_self, _self)
        {}

        //@abi action
        void addblog(string author, string title, string hash) {
            blogs.emplace(_self, [&](auto& blog) {
                blog.id = blogs.available_primary_key();
                blog.author = author;
                blog.title = title;
                blog.hash = hash;
            });
        };




    private:

        // @abi table
        struct blog {
            uint64_t id;
            string author;
            string title;
            string hash;

            uint64_t primary_key()const { return id; }
            EOSLIB_SERIALIZE(blog, (id)(author)(title)(hash))
        };
        typedef multi_index<N(blog), blog> blog_index;
        blog_index blogs;
};
EOSIO_ABI(ipfs, (addblog));
