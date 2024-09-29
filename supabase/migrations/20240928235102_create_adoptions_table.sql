CREATE TABLE public.adoptions
(
    uuid                uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    tree_uuid           uuid NOT NULL,
    user_uuid           uuid NOT NULL,
    created_at          timestamp DEFAULT CURRENT_TIMESTAMP,
    updated_at          timestamp DEFAULT CURRENT_TIMESTAMP,
    deleted_at          timestamp DEFAULT NULL,

    FOREIGN KEY (tree_uuid) REFERENCES public.trees(uuid) ON DELETE CASCADE,
    FOREIGN KEY (user_uuid) REFERENCES auth.users(id) ON DELETE CASCADE,

    UNIQUE (tree_uuid, user_uuid)
);

comment on table public.adoptions is 'Alle Informationen über die Adoptionen von Bäumen durch Nutzer.';

alter table public.adoptions
    owner to postgres;

grant select on public.adoptions to anon;

grant delete, insert, references, select, trigger, truncate, update on public.adoptions to authenticated;

grant delete, insert, references, select, trigger, truncate, update on public.adoptions to service_role;

create policy "Enable read access for all users" on "public"."adoptions" as permissive for select to public using (true);