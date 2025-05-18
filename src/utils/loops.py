import torch

from tqdm import tqdm


def train_loop(
    model, loss_fn,
    optimizer, dataloader,
    use_gpu: bool = False
):
    model.train()

    losses = []
    pbar = tqdm(dataloader, total=len(dataloader))
    for features_seq, next_seq, city_coords in pbar:
        if use_gpu:
            features_seq = features_seq.cuda()
            next_seq = next_seq.cuda()
            city_coords = city_coords.cuda()

        prediction = model(features_seq, city_coords)
        loss = loss_fn(prediction, next_seq)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        losses.append(loss.item())
        pbar.set_postfix_str(f'Loss: {losses[-1]}')
    return losses

@torch.no_grad()
def eval_loop(
    model, loss_fn,
    test_loader,
    use_gpu: bool = False
):
    model.eval()

    losses = []
    for features_seq, next_seq, city_coords in test_loader:
        if use_gpu:
            features_seq = features_seq.cuda()
            next_seq = next_seq.cuda()
            city_coords = city_coords.cuda()

        prediction = model(features_seq, city_coords)
        loss = loss_fn(prediction, next_seq)

        losses.append(loss.item())

    return losses